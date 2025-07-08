import type { InterfaceMask } from './InterfaceMask';

export class MaskData implements InterfaceMask {
  mask(value: string): string {
    value = value.replace(/\D/g, '');
    if (value.length <= 10) {
      value = value
        .replace(/(\d{2})(\d)/, '$1/$2')
        .replace(/(\d{2})(\d)/, '$1/$2');
    }
    return value;
  }
}
