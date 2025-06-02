import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
// Componente
import { Sidebar } from "@components/Sidebar";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { SelectInputForm } from "@components/Select";
import { InputComponent } from "@components/Input";
// Utils
import { veiculos } from "@utils/Selects/TipoVeiculos";
import { status } from "@utils/Selects/StatusVeiculo";
// Schemas
import { schemaCadVeiculo, type DataProps } from "@schemas/CadsVeiculos";
import { ButtonWrapper, Container, ContainerInputs } from "./styles";

export function CadastroVeiculo() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<DataProps>({
        mode: "onBlur",
        resolver: zodResolver(schemaCadVeiculo),
    });

    return (
        <Container>
            <Sidebar />
            <RegisterPageGeneric title="Cadastro de veículo">
                <form onSubmit={handleSubmit((data) => console.log(data))}>
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
                            placeholder="Ex: 03/05/2001"
                            mask="data"
                            maxLength={10}
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
                        <button type="submit">Cadastrar</button>
                    </ButtonWrapper>
                </form>
            </RegisterPageGeneric>
        </Container>
    );
}
