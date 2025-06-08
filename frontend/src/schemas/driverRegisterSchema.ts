import { z } from "zod";

const driverRegisterFormSchema = z.object({
  name: z.string().nonempty("O nome é obrigatório"),
  cpf: z.string().nonempty("CPF é obrigatório"),
  password: z.string().nonempty("Senha deve ser preenchida"),
  licenceType: z.string().nonempty("Tipo de CNH é obrigatório"),
  licenceNumber: z.string().nonempty("Num CNH é obrigatório"),
  email: z.string().email("Formato de e-mail inválido").nonempty("Email é obrigatório"),
  birthYear: z.string().nonempty("Data de nascimento é obrigatória").transform((value) => {
    return value.split(`/`).reverse().join('-');
  }),
  performance: z.preprocess((val) => {
    if (val === '' || val == null) return 10;
    const n = Number(val);
    return isNaN(n) ? 10 : n;
  }, z.number().min(0).max(10)),
});

type IDriverRegisterData = z.output<typeof driverRegisterFormSchema>

export { driverRegisterFormSchema };
export type { IDriverRegisterData };


