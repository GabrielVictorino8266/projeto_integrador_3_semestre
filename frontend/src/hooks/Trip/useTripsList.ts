import type { Trip } from "@interfaces/trips.interface";
import { getTrips } from "@services/Api/Trips/getTrips";
import { useEffect, useState } from "react";

export function useTripList() {
    const [data, setData] = useState<Trip[]>([]);
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPage] = useState(1);
    const [status, setStatus] = useState("");
    const [destination, setDestination] = useState("");

    async function fetchTrips() {
        const res = await getTrips({ page, limit: 6, destination, status:status });
        setData(res?.items ?? []);
        setTotalPage(res?.last_page ?? 1);
    }

    useEffect(() => {
        fetchTrips();
    }, [page, status, destination]);

    return { data, page, status, destination, totalPages, setPage, setStatus, setDestination, refetchTrip: fetchTrips };
}
