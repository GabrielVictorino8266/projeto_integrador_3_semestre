//Caso precisa adicionar ou retirar tipo de mascara, alterar o TypeMask.ts e FactoryMask.ts
import type { InterfaceMask } from './InterfaceMask';
import { MaskCpf } from './MaskCpf';
import { MaskData } from './MaskData';
import { MaskHours } from './MaskHours';
import { MaskKm } from './MaskKm';
import { MaskLicensePlate } from './MaskLicensePlate';
import { MaskPhone } from './MaskPhone';

export function FactoryMask(param: string): InterfaceMask {
  switch (param) {
    case 'cpf':
      return new MaskCpf();
    case 'phone':
      return new MaskPhone();
    case 'data':
      return new MaskData();
    case 'licensePlate':
      return new MaskLicensePlate();
    case 'km':
      return new MaskKm();
    case 'hours':
      return new MaskHours();
    default:
      throw new Error(`Máscara desconhecida: ${param}`);
  }
}
