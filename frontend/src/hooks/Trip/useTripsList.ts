import { useDelayedSpinner } from "@hooks/useDelaydSpinner";
import type { Trip } from "@interfaces/trips.interface";
import { getTrips } from "@services/Api/Trips/getTrips";
import { useEffect, useState } from "react";
import { toast } from "react-toastify";

export function useTripList() {
    const [data, setData] = useState<Trip[]>([]);
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPage] = useState(1);
    const [status, setStatus] = useState("");
    const [destination, setDestination] = useState("");
    const { showSpinner, startSpinner, stopSpinner } = useDelayedSpinner();

    async function fetchTrips() {
        try {
            startSpinner();
            const res = await getTrips({ page, limit: 6, destination, status });
            setData(res?.items ?? []);
            setTotalPage(res?.last_page ?? 1);
        } catch {
            toast.error("Erro ao carregar a listagem");
        } finally {
            stopSpinner();
        }
    }

    useEffect(() => {
        fetchTrips();
    }, [page, status, destination]);

    return {
        data,
        page,
        status,
        destination,
        totalPages,
        LoadingVehiclList: showSpinner,
        setPage,
        setStatus,
        setDestination,
        refetchTrip: fetchTrips,
    };
}
