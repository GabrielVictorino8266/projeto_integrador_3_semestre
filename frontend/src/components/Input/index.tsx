import { useState } from "react"
import { ContainerInput } from "./styles"
import { FactoryMask } from "../../Utils/Mask/FactoryMask"

type TypesProps = {
    text: string,
    LabelText: string,
    cadeado?: boolean,
    type: string,
    mask?: 'cpf' | 'telefone'
}

export function InputComponent(props: TypesProps){

    const [value, setValue] = useState("")

    function getChange(e:React.ChangeEvent<HTMLInputElement>) {

        if(props.mask != null){
            const instance = FactoryMask(props.mask)

            const formated = instance.mask(e.target.value)
            console.log(formated)
            setValue(formated)
        }else {
            setValue(e.target.value)
        }
    }

    return (
        <div>
            <ContainerInput cadeado={props.cadeado}>
                <label>{props.LabelText}</label>

                <input  type={props.type}
                        placeholder={props.text}
                        value={value}
                        onChange={getChange}
                        maxLength={14}
                    />            
            </ContainerInput>
        </div>
    ) 

}