import { normalizeFormDate } from "@utils/reserve";
import { z } from "zod";

const tripCreateFormSchema = z.object({
  driverId: z.string().nonempty("Selecione um motorista"),
  vehicleId: z.string().nonempty("Selecione um motorista"),
  initialKm: z.number().nonnegative("Nao pode ser negativo"),
  tripDate: z
    .string()
    .nonempty("A data da viagem é obrigatória")
    .transform((date) => {
      return normalizeFormDate(date);
    }),
  tripHour: z
    .string()
    .nonempty("A hora da viagem é obrigatória")
    .transform((hour) => {
      return `${hour}:00-03:00`;
    }),
  origin: z.string().nonempty("Local de origem é obrigatório"),
  destination: z.string().nonempty("Destino da viagem é obrigaatório"),
  status: z.string().nonempty("Status é obrigatório"),
});

export { tripCreateFormSchema };
