import { FactoryMask } from "./FactoryMask";
import type { MaskType } from "./TypeMask";

export function ApplyMask(event: React.ChangeEvent<HTMLInputElement>, mask?: MaskType): string {
    const valueChange = event.target.value;

    if (mask) {
        const instancia = FactoryMask(mask);
        const formatted = instancia.mask(valueChange);
        return formatted;
    }

    return valueChange;
}
