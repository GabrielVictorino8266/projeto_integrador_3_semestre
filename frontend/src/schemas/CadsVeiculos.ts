import { z } from "zod";

const currentYear = new Date().getFullYear();

export const schemaCadVeiculo = z
    .object({
        vehicleNumber: z.string(),
        licensePlate: z
            .string()
            .min(7, "Digite uma placa válida")
            .max(8)
            .regex(
                /^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$/,
                "Formato de placa inválido"
            ),

        vehicleType: z.string().min(1, "Escolha uma opção"),
        manufacturingYear: z
            .string()
            .min(4, "Deve ter no mínimo 4 caracteres")
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
        brand: z.string(),
        currentKm: z.coerce.number().min(0, "Adiciona um KM"),
        warningKmLimit: z.coerce.number().min(0, "Adicione um KM"),
        status: z.string().min(1, "Escolha uma opção"),
    })
    .required();

export type DataProps = z.infer<typeof schemaCadVeiculo>;
