import { Sidebar } from "../../../components/Sidebar" 
import { Container, Main, Header, Form, BoxForm } from "./styles"

export function CadastroVeiculo(){
    return(

        <Container>
            <Sidebar />  
            <Main>
                <Header>
                    <h1>Cadastro de viagem</h1>
                </Header>
                
                <BoxForm>
                    <Form>
                        
                    </Form>
                </BoxForm>

            </Main>  
        </Container>
        
    )
}