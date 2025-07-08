import type { InterfaceMask } from './InterfaceMask';

export class MaskHours implements InterfaceMask {
  mask(value: string): string {
    value = value.replace(/\D/g, '');

    if (value.length >= 3) {
      return value.replace(/(\d{2})(\d{1,2})/, '$1:$2');
    }

    return value;
  }
}
