import { getTrips } from "@services/Api/Trips/getTrips";
import { useEffect, useState } from "react";

export function useTripsStats() {
    const [completed, setCompleted] = useState(0);
    const [inProgress, setInProgress] = useState(0);
    const [scheduled, setScheduled] = useState(0);
    const [total, setTotal] = useState(0);

    async function fetchStats() {
        const [all, conc, sched, prog] = await Promise.all([
            getTrips({ limit: 1 }),
            getTrips({ status: "completed", limit: 1 }),
            getTrips({ status: "scheduled", limit: 1 }),
            getTrips({ status: "in_progress", limit: 1 }),
        ]);
        setTotal(all?.total ?? 0);
        setCompleted(conc?.total ?? 0);
        setScheduled(sched?.total ?? 0);
        setInProgress(prog?.total ?? 0);
    }

    useEffect(() => {
        fetchStats();
    }, []);

    return { total, completed, inProgress, scheduled, refetchTripsStatus: fetchStats };
}
