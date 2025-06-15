import { z } from "zod";

const currentYear = new Date().getFullYear();

export const schemaCadVeiculo = z
    .object({
        vehicleNumber: z.string(),
        licensePlate: z
          .string()
          .transform((val) => val.replace("-", "").toUpperCase())
          .refine(
            (val) => /^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$/.test(val),
            { message: "Formato de placa inválido" }
          ),
        vehicleType: z.string().min(1, "Escolha uma opção"),
        manufacturingYear: z.coerce
            .number()
            .int("Apenas números inteiros")
            .gte(1000, "Deve conter 4 dígitos")
            .lte(9999, "Deve conter 4 dígitos")
            .refine((ano) => ano >= 1900 && ano <= currentYear + 1, {
                message: `Ano do veículo deve estar entre 1900 e ${
                    currentYear + 1
                }`,
            }),
        brand: z.string(),
        currentKm: z.string().min(1, "Adiciona um KM"),
        warningKmLimit: z.string().min(1, "Adicione um KM"),
        status: z.string().min(1, "Escolha uma opção"),
    })
    .required();

export type DataProps = z.infer<typeof schemaCadVeiculo>;
