import { FactoryMask } from "./FactoryMask";
import type { MaskType } from "./TypeMask";

export function ApplyMask(
    event: React.ChangeEvent<HTMLInputElement>,
    mask: MaskType | undefined,
    setValue: (val: string) => void
) {
  const valueChange = event.target.value;

  if (mask) {
      const instancia = FactoryMask(mask);
      const formatted = instancia.mask(valueChange);
      setValue(formatted);
  } else {
      setValue(valueChange);
  }
}
