import { RegInput } from "@components/InputForm";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  driverRegisterFormSchema,
  type IDriverRegisterData,
} from "@schemas/driverRegisterSchema";
import { useForm, type FieldError, type SubmitHandler } from "react-hook-form";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { Button } from "@styles/Buttons";
import { SelectInputForm } from "@components/Select";
import { cnhCategories } from "@utils/Selects/cnhCategories";
import { ContainerInputs } from "./styles";
import { useDriver } from "@hooks/useDriver";
import { MaskPhone } from "@utils/Mask/MaskPhone";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const DriverUpdate = () => {
  const {
    handleCreateDriver,
    inputDate,
    inputValue,
    handleDateMask,
    handleInputMask,
    getDriverByID,
    driverUnderEdition,
    setDriverUnderEdition,
  } = useDriver();
  const { id } = useParams();

  useEffect(() => {
    getDriverByID(id!);
    return () => {
      setDriverUnderEdition(null);
    };
  }, []);

  console.log(driverUnderEdition);

  const [phoneValue, setPhoneValue] = useState<string>("");

  const maskPhone = new MaskPhone();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(driverRegisterFormSchema),
  });

  const submitDriver: SubmitHandler<IDriverRegisterData> = async (
    registerForm: IDriverRegisterData
  ) => {
    registerForm.phone = registerForm.phone.replace(/\D/g, "");
    registerForm.cpf = registerForm.cpf.replace(/\D/g, "");
    handleCreateDriver(registerForm); // TROCAR PARA UPDATEDRIVER
    console.log(registerForm);
  };

  return (
    <RegisterPageGeneric title="Editar motorista">
      <form onSubmit={handleSubmit(submitDriver)}>
        <ContainerInputs>
          <RegInput
            type={"text"}
            placeholder={"Digite o nome do motorista"}
            id={"nome"}
            label={"Nome"}
            {...register("name")}
            error={errors.name}
            defaultValue={driverUnderEdition?.name}
          />
          <SelectInputForm
            optionsArray={cnhCategories}
            label={"Carteira de Habilitaçao"}
            {...register("licenceType")}
            error={errors.licenceType}
          />
          <RegInput
            type={"text"}
            placeholder={"xxx.xxx.xxx-xx"}
            id={"cpf"}
            label={"CPF"}
            {...register("cpf")}
            error={errors.cpf}
            value={inputValue}
            onChange={handleInputMask}
          />
          <RegInput
            type={"number"}
            placeholder={"Numero da habilitação"}
            id={"licenceNumber"}
            label={"Número CNH"}
            {...register("licenceNumber")}
            error={errors.licenceNumber}
          />
          <RegInput
            type={"password"}
            placeholder={"Digite a senha do motorista"}
            id={"password"}
            label={"Senha"}
            {...register("password")}
            error={errors.password}
          />
          <RegInput
            type={"number"}
            placeholder={"Ex: 5"}
            id={"performance"}
            label={"Aproveitamento"}
            {...register("performance", { valueAsNumber: true })}
            error={errors.performance as FieldError}
          />
          <RegInput
            type={"text"}
            placeholder={"(XX) XXXXX-XXXX"}
            id={"phone"}
            label={"Telefone"}
            {...register("phone")}
            error={errors.phone}
            value={phoneValue}
            onChange={(event) => {
              setPhoneValue(maskPhone.mask(event.target.value));
            }}
          />
          <RegInput
            type={"text"}
            placeholder={"Data de nascimento"}
            id={"birthYear"}
            label={"Data de nascimento"}
            {...register("birthYear")}
            error={errors.birthYear}
            value={inputDate}
            onChange={handleDateMask}
          />
        </ContainerInputs>
        <div className="form__sendButton">
          <Button>ATUALIZAR</Button>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { DriverUpdate };
