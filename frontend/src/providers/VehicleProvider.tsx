// src/contexts/vehicle.provider.tsx
import { useEffect, useState } from "react";
import { VehicleContext } from "@contexts/vehicles.context";
import { getVehicles } from "@services/Api/Vehicles/getVehicle"; // <- essa é a função que você criou
import type { IVehicle } from "@interfaces/vehicles.interface";
import { toast } from "react-toastify";

export const VehicleProvider = ({
    children,
}: {
    children: React.ReactNode;
}) => {
    const [vehicleList, setVehicleList] = useState<IVehicle[]>([]);
    const [vehicleQuantity, setVehicleQuantity] = useState(0);
    const [vehicleActive, setVehicleActive] = useState(0);
    const [vehicleInactive, setVehicleInactive] = useState(0);

    async function getVehicleList() {
        const data = await getVehicles();
        if (!data) return;

        const list = data.items;
        setVehicleList(list);

        const qtde = list.length;
        const active = list.filter((v) => v.status === "active").length;
        setVehicleActive(active);
        setVehicleQuantity(qtde);
        setVehicleInactive(qtde - active);

        toast.success("Lista de veículos carregaduuuu!");
    }

    useEffect(() => {
        getVehicleList();
    }, []);

    return (
        <VehicleContext.Provider
            value={{
                getVehicleList,
                vehicleList,
                vehicleQuantity,
                vehicleActive,
                vehicleInactive,
            }}
        >
            {children}
        </VehicleContext.Provider>
    );
};
