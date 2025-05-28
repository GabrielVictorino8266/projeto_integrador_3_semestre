import { z } from "zod";

const driverRegisterFormSchema = z.object({
  name: z.string().nonempty("O nome é obrigatório"),
  cpf: z.string().nonempty("CPF é obrigatório"),
  password: z.string().nonempty("Senha deve ser preenchida"),
  cnh: z.string().nonempty("CNH é obrigatória"),
});

type IDriverRegisterData = z.infer<typeof driverRegisterFormSchema>;

export type { IDriverRegisterData };
export { driverRegisterFormSchema };
