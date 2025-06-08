import type { DataProps } from "@schemas/CadsVeiculos";
import { useEffect, useState } from "react";
import { formatDateToBR } from "@utils/Mask/FormatDateToBR";
import { getVehiclesId } from "@services/Api/Registration/GetVehiclesId";

export function useFetchVeiculos(
    id: string | undefined,
    reset: (velues: DataProps) => void
) {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!id) {
            setLoading(false);
            return;
        }

        // const fetchData = async ( ) => {
        //     try{
        //         const response = await getVehiclesId(id)

        //         const veiculo = {
        //             ...response,
        //              anoVeiculo: formatDateToBR(response.anoVeiculo),
        //         }
        //         reset(veiculo)
        //     }catch(error){
        //         console.log("Erro")
        //     }finally{
        //         setLoading(false)
        //     }
        // }
        
        const timer = setTimeout(() => {
            if (id === "1") {
                const mockVeiculo: DataProps = {
                    placa: "ABC1234",
                    marca: "Volkswagen",
                    numero: "42",
                    anoVeiculo: "2015-05-15",
                    tipoVeiculo: "Onibus",
                    status: "manutencao",
                };

                mockVeiculo.anoVeiculo = formatDateToBR(mockVeiculo.anoVeiculo);

                reset(mockVeiculo);
            } else {
                console.warn(`ID ${id} não encontrado`);
            }

            setLoading(false);
        }, 0);

        // fetchData()
        return () => clearTimeout(timer);
    }, [id, reset]);

    return { loading };
}
