import { normalizeFormDate } from "@utils/reserve";
import { z } from "zod";

const tripCreateFormSchema = z.object({
  driver: z.string().nonempty("Selecione um motorista"),
  tripDate: z
    .string()
    .nonempty("Escolha uma data")
    .transform((tripDate) => {
      return normalizeFormDate(tripDate);
    }),
});

export { tripCreateFormSchema };
