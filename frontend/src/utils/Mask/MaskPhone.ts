import type { InterfaceMask } from "./InterfaceMask";


export class MaskPhone implements InterfaceMask{
    mask(value: string): string {

        value = value.replace(/\D/g, '');
        if (value.length <= 11) {
            value = value
            .replace(/(\d{2})(\d)/, '($1) $2')
            .replace(/(\d{5})(\d)/, '$1-$2')
        }
        return value;
        
    }
}