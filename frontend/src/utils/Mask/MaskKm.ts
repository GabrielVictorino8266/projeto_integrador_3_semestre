import type { InterfaceMask } from "./InterfaceMask";

export class MaskKm implements InterfaceMask {
    mask(value: string): string {
        const onlyNumbers = value.replace(/\D/g, "");
        return new Intl.NumberFormat("pt-BR").format(Number(onlyNumbers));
    }

}
