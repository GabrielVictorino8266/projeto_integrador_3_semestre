import { ContainerInput } from "./styles"
import { FactoryMask } from "../../Utils/Mask/FactoryMask"

type TypesProps = {
    text: string,
    LabelText: string,
    cadeado?: boolean,
    type: string,
    mask?: 'cpf' | 'telefone'
    value?: string,
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    name?: string;
    inputRef: React.Ref<HTMLInputElement>
}

export function InputComponent(props: TypesProps){

    function getChange(e:React.ChangeEvent<HTMLInputElement>) {

        if(props.mask != null){
            const instance = FactoryMask(props.mask)
            const formated = instance.mask(e.target.value)

            const customEvnt ={
                ...e,
                target:{
                    ...e.target,
                    value: formated,
                    name: props.name || ''
                }
            }

            props.onChange(customEvnt as React.ChangeEvent<HTMLInputElement>)

        }else {
            props.onChange?.(e)
        }
    }

    return (
        <div>
            <ContainerInput cadeado={props.cadeado}>
                <label>{props.LabelText}</label>

                <input  type={props.type}
                        placeholder={props.text}
                        value={props.value || ""}
                        onChange={getChange}
                        name={props.name}
                        ref={props.inputRef}
                        maxLength={14}
                    />            
            </ContainerInput>
        </div>
    ) 

}