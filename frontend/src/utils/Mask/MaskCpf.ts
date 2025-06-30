import type { InterfaceMask } from './InterfaceMask';

export class MaskCpf implements InterfaceMask {
  mask(value: string): string {
    value = value.replace(/\D/g, '');
    if (value.length <= 11) {
      value = value
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    }
    return value;
  }
}
