import type { DataProps } from "@schemas/CadsVeiculos";
import { useEffect, useState } from "react";
import { getVehiclesId } from "@services/Api/Vehicles/GetVehiclesId";

export function useFetchVeiculos(id: string | undefined, reset: (values: DataProps) => void) {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!id) {
            setLoading(false);
            return;
        }
        const fetchData = async () => {
            try {
                const response = await getVehiclesId(id);
                if (response) {
                    reset(response);
                }
            } catch (error) {
                console.log("Erro");
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [id, reset]);

    return { loading };
}
