import { z } from "zod";

const tripFormSchema = z
  // TO-DO: ADAPTAR COM OS NOMES DOS CAMPOS QUE PRECISAM SER ENVIADOS PARA A API
  .object({
    driver: z.string().nonempty("O motorista é obrigatório"),
    vehicle: z.string().nonempty("O veículo é obrigatório"),
    tripDate: z.string().nonempty("A data é obrigatória"),
    hour: z.string().nonempty("O horário é obrigatório"),
    startPoint: z.string().min(1, "Escolha uma opção"),
    status: z.string().nonempty("Selecione um status"),
  });

export { tripFormSchema };
export type ITripFormRegister = z.infer<typeof tripFormSchema>;
