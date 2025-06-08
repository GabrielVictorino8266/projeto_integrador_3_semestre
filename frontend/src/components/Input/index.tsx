import { ApplyMask } from '@utils/Mask/ApplyMask'
import type { MaskType } from '@utils/Mask/TypeMask';
import { ContainerInput } from "./styles";
import { forwardRef, useId, useState, type InputHTMLAttributes } from "react";

type InputProps = InputHTMLAttributes<HTMLInputElement>  &{
  label?: string;
  errorMessage?: string
  mask?: MaskType; //Caso precisa adicionar ou retirar tipo de mascara, alterar os arquivos TypeMask.ts e FactoryMask.ts
  cadeado?: boolean;
  pessoa?: boolean;
};

export const InputComponent = forwardRef<HTMLInputElement, InputProps>(({type = 'text', name = '', label = '', errorMessage = '', mask, pessoa, cadeado, ...props }, ref) => {
    const InputId = useId()
    const [value, setValue ] = useState<string>('')

    return(
        <div>
            <ContainerInput  cadeado={cadeado} pessoa={pessoa} error={errorMessage}>
                {label && <label htmlFor={InputId}>{label}</label>}
                  
                <input
                    id={InputId}
                    type={type}
                    name={name}
                    ref={ref}
                    {...props}
                    onChange={(e) => ApplyMask(e, mask, setValue)}
                    value={value}
                />

                {errorMessage && <p>{errorMessage}</p> } 
            </ContainerInput>
        </div>
    )
})

