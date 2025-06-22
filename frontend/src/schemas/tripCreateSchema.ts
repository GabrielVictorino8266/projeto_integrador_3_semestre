import { normalizeFormDate } from "@utils/reserve";
import { z } from "zod";

const tripCreateFormSchema = z.object({
  driverId: z.string().nonempty("Selecione um motorista"),
  vehicleId: z.string().nonempty("Selecione um motorista"),
  startDateTime: z.string().nonempty("A hora de início é obrigatória"),
  origin: z.string().nonempty("Local de origem é obrigatório"),
  destination: z.string().nonempty("Destino da viagem é obrigaatório"),
  initialKm: z.string().nonempty("Quilometragem inicial é obrigatória"),

  tripDate: z
    .string()
    .nonempty("Escolha uma data")
    .transform((tripDate) => {
      return normalizeFormDate(tripDate);
    }),
  status: z.string().nonempty("Status é obrigatório"),
});

export { tripCreateFormSchema };
