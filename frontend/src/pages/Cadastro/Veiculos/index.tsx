import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate, useParams } from "react-router-dom";
import { useForm } from "react-hook-form";
// Componente
import { Sidebar } from "@components/Sidebar";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { SelectInputForm } from "@components/Select";
import { InputComponent } from "@components/Input";
// Utils
import { veiculos } from "@utils/Selects/TipoVeiculos";
import { status } from "@utils/Selects/StatusVeiculo";
// hooks
import { useFetchVeiculos } from "@hooks/useFetchVeiculos/index";
// Schemas
import { schemaCadVeiculo, type DataProps } from "@schemas/CadsVeiculos";
// Service
import { VehiclesRegistration } from "@services/Api/Registration/VehiclesRegistration";
// Styles
import { ButtonWrapper, Container, ContainerInputs } from "./styles";

export function CadastroVeiculo() {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const currentYear = new Date().getFullYear();
    const {
        register,
        handleSubmit,
        formState: { errors },
        reset,
    } = useForm<DataProps>({
        mode: "onBlur",
        resolver: zodResolver(schemaCadVeiculo),
    });

    const { loading } = useFetchVeiculos(id, reset);

    if (loading) return <p>Carregando...</p>;

    const Submit = async (data: DataProps) => {
        const sucess = await VehiclesRegistration(data, id);
        setTimeout(() => {
            navigate("/dashboard");
        }, 1800);
        console.log(sucess);
        console.log("Cadastrado", data);
    };

    return (
        <Container>
            <Sidebar />
            <RegisterPageGeneric title="Cadastro de veículo">
                <form onSubmit={handleSubmit(Submit)}>
                    <ContainerInputs>
                        <InputComponent
                            label="Placa"
                            {...register("placa")}
                            placeholder="Placa do veículo"
                            maxLength={7}
                            errorMessage={errors.placa?.message}
                        />
                        <InputComponent
                            label="Marca"
                            {...register("marca")}
                            placeholder="Marca"
                            errorMessage={errors.marca?.message}
                        />
                        <InputComponent
                            label="Número"
                            {...register("numero")}
                            placeholder="Número do veículo"
                            errorMessage={errors.numero?.message}
                        />
                        <InputComponent
                            label="Ano do veículo"
                            {...register("anoVeiculo")}
                            placeholder={`Ex: ${currentYear}`}
                            maxLength={4}
                            errorMessage={errors.anoVeiculo?.message}
                        />
                        <SelectInputForm
                            label="Tipo de veículo"
                            optionsArray={veiculos}
                            {...register("tipoVeiculo")}
                            error={errors.tipoVeiculo}
                        />
                        <SelectInputForm
                            label="Status"
                            optionsArray={status}
                            {...register("status")}
                            error={errors.status}
                        />
                    </ContainerInputs>

                    <ButtonWrapper>
                        <button type="submit">
                            {id ? "Atualizar" : "Cadastrar"}
                        </button>
                    </ButtonWrapper>
                </form>
            </RegisterPageGeneric>
        </Container>
    );
}

