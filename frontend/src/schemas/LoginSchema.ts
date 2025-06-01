import { z } from "zod";

export const LoginSchema = z
  .object({
    cpf: z
      .string({ required_error: "CPF é obrigatório" })
      .min(14, "CPF Inválido"),
    password: z
      .string({ required_error: "Senha é obrigatória" })
      .min(6, "A senha precisa ter no mínimo 6 caracteres"),
  })
  .required();

export type DataProps = z.infer<typeof LoginSchema>