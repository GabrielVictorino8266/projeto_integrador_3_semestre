import { Sidebar } from "@components/Sidebar" 
import { BoxInput, Container, RightContainer, Template } from "./styles"
import {HeaderCadastro} from '@components/Header'

export function CadastroVeiculo(){
    return(

        <Container>
            <Sidebar />
            <RightContainer>
                <HeaderCadastro Title="Cadastro de veículos" />

                <Template>
                    <BoxInput>
                        <h1>oi</h1>
                    </BoxInput>
                </Template>
            </RightContainer>
        </Container>
        
    )
}