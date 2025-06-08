import { z } from "zod";

const currentYear = new Date().getFullYear();

export const schemaCadVeiculo = z
    .object({
        placa: z.string().min(7, "Digite uma placa de carro válida"),
        marca: z.string(),
        numero: z.string(),
        anoVeiculo: z
            .string()
            .min(4, "Deve ter no minimo 4 caracteres")
            .max(4, "No máximo 4 caracteres")
            .refine(
                (val) => {
                    const ano = Number(val);
                    return ano >= 1900 && ano <= currentYear + 1;
                },
                {
                    message: `Ano do veículo deve estar entre 1900 e ${
                        currentYear + 1
                    }`,
                }
            ),
        tipoVeiculo: z.string().min(1, "Escolha uma opção"),
        status: z.string().min(1, "Escolha uma opção"),
    })
    .required();

export type DataProps = z.infer<typeof schemaCadVeiculo>;
