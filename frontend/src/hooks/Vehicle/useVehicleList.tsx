import { useEffect, useState } from "react";
import { getVehicles } from "@services/Api/Vehicles/getVehicle";
import type { IVehicle, VehicleStatus } from "@interfaces/vehicles.interface";
import { toast } from "react-toastify";
import { useDelayedSpinner } from "@hooks/useDelaydSpinner";

export const useVehicleList = () => {
    const [data, setData] = useState<IVehicle[]>([]);
    const [page, setPage] = useState(1);
    const [status, setStatus] = useState<VehicleStatus | null>(null);
    const [totalPages, setTotalPages] = useState(1);
    const [plate, setPlate] = useState("");
    const { showSpinner, startSpinner, stopSpinner } = useDelayedSpinner();

    async function fetchList() {
        try{
            startSpinner()
            const res = await getVehicles({ page:page, status: status ?? undefined, licensePlate:plate });
            setData(res?.items ?? []);
            setTotalPages(res?.last_page ?? 1);
        }catch{
            toast.error("Erro ao carregar os dados")
        }finally{
            stopSpinner();
        }
    }

    useEffect(() => {
        fetchList();
    }, [page, status, plate]);

    return { data, page, plate, status, LoadingList:showSpinner , setStatus, setPage, setPlate,refetch: fetchList, totalPages };
};
