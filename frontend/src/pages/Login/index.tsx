import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router-dom";
// Assets
import Logo from "@assets/Logo.png";
// Componentes
import { InputComponent } from "@components/Input";
// Schemas
import { LoginSchema } from "@schemas/LoginSchema";
import type { DataProps } from "@schemas/LoginSchema";
// Services
import { LoginRequest } from "@services/Api/LoginRequest";
// Estilos
import {
    Container,
    LeftContainer,
    RightContainer,
    TitleDiv,
    Links,
    BotaoEntrar,
    ConainerLift,
} from "./Styles";

export function Login() {
    const navigate = useNavigate();

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<DataProps>({
        resolver: zodResolver(LoginSchema),
    });

    const Submit = async (data: DataProps) => { 
        const response = await LoginRequest(data)
        if(response){
            setTimeout(() => {
                navigate("/dashboard")
            }, 2000);
        }
    };

    return (
        <Container>
            <LeftContainer>
                <ConainerLift>
                    <TitleDiv>
                        <img src={Logo} alt="Logo-Viação-União" />
                        <h1>
                            Viação <br />
                            <span>UNIÃO</span>
                        </h1>
                    </TitleDiv>

                    <form onSubmit={handleSubmit(Submit)}>
                        <InputComponent
                            {...register("cpf")}
                            type="text"
                            label="CPF"
                            placeholder="Digite seu CPF"
                            maxLength={14}
                            mask="cpf"
                            pessoa={true}
                            errorMessage={errors.cpf?.message}
                        />

                        <br />

                        <InputComponent
                            {...register("password")}
                            type="password"
                            label="Senha"
                            placeholder="Digite sua senha"
                            cadeado={true}
                            errorMessage={errors.password?.message}
                        />

                        <Links>
                            <a href="">Esqueci minha senha</a>
                            <a href="">Cadastre-se</a>
                        </Links>

                        <BotaoEntrar type="submit">ENTRAR</BotaoEntrar>
                    </form>
                </ConainerLift>
            </LeftContainer>
            <RightContainer />
        </Container>
    );
}
