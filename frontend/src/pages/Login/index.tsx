import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
// Services
import { api } from "@services/api";
// Assets
import Logo from "@assets/Logo.png";
// Componentes
import { InputComponent } from "@components/Input";
// schemas
import { LoginSchema } from "@schemas/LoginSchema";
import type { DataProps } from "@schemas/LoginSchema";
// Utils
import { ClearMask } from "@utils/Mask/ClearMask";
// estilos
import {
    Container,
    LeftContainer,
    RightContainer,
    TitleDiv,
    Links,
    BotaoEntrar,
    ConainerLift,
} from "./Styles";
import { zodResolver } from "@hookform/resolvers/zod";

export function Login() {
    const navigate = useNavigate();

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<DataProps>({
        mode: "onBlur",
        resolver: zodResolver(LoginSchema),
    });

    const Submit = async (data: DataProps) => {
        const cpf = ClearMask(data.cpf);
        console.log(cpf);
        const response = await toast.promise(
            api.post("/users/login/", {
                cpf: cpf,
                password: data.password,
            }),
            {
                pending: "Verificando dados",
                success: {
                    render() {
                        setTimeout(() => {
                            navigate("/dashboard");
                        }, 2000);
                        return "Seja bem vinde";
                    },
                },
                error: "CPF ou senha incorretos",
            }
        );
        console.log(response);
        localStorage.clear();
        localStorage.setItem("token", response.data.access_token);
        localStorage.setItem("nome", response.data.user.name);
        localStorage.setItem("cargo", response.data.user.type);
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
