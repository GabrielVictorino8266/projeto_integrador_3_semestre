import type { InterfaceMask } from "./InterfaceMask";
import { MaskCpf } from "./MaskCpf";
import { MaskPhone } from "./MaskPhone";


export function FactoryMask(param: string ):InterfaceMask{

    switch (param) {
        case "cpf":
            return new MaskCpf()    
        case "phone":
            return new MaskPhone()
        
        default:
            throw new Error(`Máscara desconhecida: ${param}`)
    }

}