import { z } from "zod";

export const schemaCadVeiculo = z
    .object({
        placa: z.string().min(7, "Digite uma placa de carro válida"),
        marca: z.string(),
        numero: z.string(),
        anoVeiculo: z.string(),
        tipoVeiculo: z.string().min(1,"Escolha uma opção"),
        status: z.string().min(1, "Escolha uma opção"),
    })
    .required();

export type DataProps = z.infer<typeof schemaCadVeiculo>;
