import { useForm, Controller } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { useNavigate } from "react-router-dom";
import {
  Container,
  LeftContainer,
  RightContainer,
  TitleDiv,
  Links,
  BotaoEntrar,
  ContainerInput
} from "./Styles";
import { toast, ToastContainer } from "react-toastify";
// import { api } from "../../services/api";
import Logo from '../../assets/Logo.png';
import { formatCPF } from "../../Utils/FormatterCPF";

const schema = yup.object({
  cpf: yup.string().required("Digite o seu CPF").min(14, "CPF inválido"),
  password: yup.string().required("Digite sua senha"),
}).required();

type FormData = {
  cpf: string;
  password: string;
};

export function Login() {
    
    const navigate = useNavigate();

    const {
        control,
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<FormData>({
        resolver: yupResolver(schema),
    });

    const onSubmit = (data: FormData) => {
        console.log("Dadus enviados:", data);
        toast.success("Login enviado com sucesso!")
        setTimeout(() => {
            navigate("/")
        },2000)
    };

    return (
        <Container>
        <LeftContainer>
            <TitleDiv>
                <img src={Logo} alt="Logo-Viação-União" />
                <h1>Viação <br /><span>UNIÃO</span></h1>
            </TitleDiv>

            <form onSubmit={handleSubmit(onSubmit)}>
            <ContainerInput cadeado={false}>
                <label>CPF</label>
                <Controller
                name="cpf"
                control={control}
                defaultValue=""
                render={({ field }) => (
                    <input
                    type="text"
                    placeholder="Digite seu CPF"
                    value={field.value}
                    onChange={(e) => field.onChange(formatCPF(e.target.value))}
                    maxLength={14}
                    />
                )}
                />
                <p>{errors.cpf?.message}</p>
            </ContainerInput>

            <ContainerInput cadeado={true}>
                <label>Senha</label>
                <input
                type="password"
                placeholder="Digite sua senha"
                {...register("password")}
                />
                <p>{errors.password?.message}</p>
            </ContainerInput>

            <Links>
                <a href="">Esqueci minha senha</a>
                <a href="">Cadastre-se</a>
            </Links>

            <BotaoEntrar type="submit">ENTRAR</BotaoEntrar>
            </form>
        </LeftContainer>
        <RightContainer />
        <ToastContainer />
        </Container>
    );
}
