import { api } from "@services/api";
import type { AxiosResponse } from "axios";
import { useEffect, useState } from "react";
import { Outlet, Navigate } from "react-router-dom";
import { toast } from "react-toastify";

interface IRefreshToken {
  access_token: string;
}

const ProtectedRoutes = () => {
  const token = localStorage.getItem("token");
  const refreshToken = localStorage.getItem("refresh_token");
  const refreshTokenBody = { refresh_token: refreshToken };
  const [isAuthorized, setIsAuthorized] = useState<boolean | null>(null);

  useEffect(() => {
    verifyToken();
  }, []);

  const verifyToken = async () => {
    if (!token) {
      setIsAuthorized(false);
      return;
    } else {
      userAuthToken();
    }
  };

  const userAuthToken = async () => {
    try {
      const refreshTokenResponse: AxiosResponse<IRefreshToken> = await api.post(
        "/users/refresh-token/",
        refreshTokenBody
      );

      if (refreshTokenResponse.status === 200) {
        localStorage.setItem("token", refreshTokenResponse.data.access_token);
        setIsAuthorized(true);
      }
    } catch (error) {
      console.log(error);
      toast.error("Acesso não autorizado. Por favor, faça login.");
      setIsAuthorized(false);
    }
  };

  if (isAuthorized === null) {
    return null;
  }

  return isAuthorized ? <Outlet /> : <Navigate to="/login" />;
};

export { ProtectedRoutes };
