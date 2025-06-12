import { normalizeDate, normalizeFormString } from "@utils/reserve";
import { z } from "zod";

const driverRegisterFormSchema = z.object({
  name: z.string().nonempty("O nome é obrigatório"),
  cpf: z
    .string()
    .nonempty("CPF é obrigatório")
    .transform((cpf) => {
      return normalizeFormString(cpf);
    }),
  password: z.string().nonempty("Senha deve ser preenchida"),
  licenseType: z.string().nonempty("Tipo de CNH é obrigatório"),
  licenseNumber: z
    .string()
    .nonempty("Num CNH é obrigatório")
    .transform((licenseNumber) => {
      return normalizeFormString(licenseNumber);
    }),
  phone: z
    .string()
    .nonempty("Telefone é obrigatório")
    .transform((phone) => {
      return normalizeFormString(phone);
    }),
  birthYear: z
    .string()
    .nonempty("Data de nascimento é obrigatória")
    .transform((value) => {
      return normalizeDate(value);
    }),
  performance: z.preprocess((val) => {
    if (val === "" || val == null) return 10;
    const n = Number(val);
    return isNaN(n) ? 10 : n;
  }, z.number().min(0).max(10)),
});

export { driverRegisterFormSchema };
