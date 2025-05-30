import { Container } from "./styles";

type propsHeader = {
    Title: string;
}

export function HeaderCadastro({ Title} : propsHeader){

    return(
        <Container>
            <h1>{Title}</h1>
        </Container>
    )

}