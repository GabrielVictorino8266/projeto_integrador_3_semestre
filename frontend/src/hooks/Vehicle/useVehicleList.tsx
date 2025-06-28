import { useEffect, useState } from "react";
import { getVehicles } from "@services/Api/Vehicles/getVehicle";
import type { IVehicle, VehicleStatus } from "@interfaces/vehicles.interface";
import { toast } from "react-toastify";

export const useVehicleList = () => {
    const [data, setData] = useState<IVehicle[]>([]);
    const [page, setPage] = useState(1);
    const [status, setStatus] = useState<VehicleStatus | null>(null);
    const [totalPages, setTotalPages] = useState(1);
    const [plate, setPlate] = useState("");
    const [LoadingList, SetLoadingList ] = useState(true)

    async function fetchList() {
        try{
            const res = await getVehicles({ page:page, status: status ?? undefined, licensePlate:plate });
            setData(res?.items ?? []);
            setTotalPages(res?.last_page ?? 1);
        }catch{
            toast.error("Erro ao carregar os dados")
        }finally{
            SetLoadingList(false)
        }
    }

    useEffect(() => {
        fetchList();
    }, [page, status, plate]);

    return { data, page, plate, status, LoadingList , setStatus, setPage, setPlate,refetch: fetchList, totalPages };
};
