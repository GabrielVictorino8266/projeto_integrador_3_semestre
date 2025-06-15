import type { InterfaceMask } from "./InterfaceMask";

export class MaskLicensePlate implements InterfaceMask {
    mask(value: string): string {
        value = value.toUpperCase().replace(/[^A-Z0-9]/g, "");

        if (value.length <= 7) {
            return value.replace(/^([A-Z]{3})([0-9]{1,4})$/, "$1-$2");
        }

        return value.slice(0, 7);
    }
}
