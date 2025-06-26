import { RegInput } from "@components/InputForm";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm, type FieldError, type SubmitHandler } from "react-hook-form";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { DarkBlueButton } from "@styles/Buttons";
import { SelectInputForm } from "@components/Select";
import { cnhCategories } from "@utils/Selects/cnhCategories";
import { ContainerInputs } from "./styles";
import { useDriver } from "@hooks/useDriver";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  driverUpdateSchema,
  type IUpdateDriver,
} from "@schemas/driverUpdateSchema";
import { cpfMask, dateMask, phoneMask } from "@utils/reserve";
import { userStatus } from "@utils/Selects/userStatus";
import { TbEdit } from "react-icons/tb";

const DriverUpdate = () => {
  const [driverName, setDriverName] = useState<string>();
  const [cpfValue, setcpfValue] = useState<string>();
  const [phoneValue, setPhoneValue] = useState<string>();
  const [birthYear, setBirthYear] = useState<string>();

  const {
    updateDriver,
    getDriverByID,
    driverUnderEdition,
    setDriverUnderEdition,
  } = useDriver();

  const { id } = useParams();

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(driverUpdateSchema),
  });

  useEffect(() => {
    if (id) {
      getDriverByID(id);
    }
    return () => setDriverUnderEdition(null);
  }, [id]);

  useEffect(() => {
    if (driverUnderEdition) {
      setValue("name", driverUnderEdition.name);
      setValue("cpf", cpfMask(driverUnderEdition.cpf));
      setValue("licenseType", driverUnderEdition.licenseType);
      setValue("licenseNumber", driverUnderEdition.licenseNumber);
      setValue("phone", phoneMask(driverUnderEdition.phone));
      setValue(
        "birthYear",
        dateMask(driverUnderEdition.birthYear.split("-").reverse().join(""))
      );
      setValue("performance", driverUnderEdition.performance);

      setValue("isActive", driverUnderEdition.isActive.toString());
    }
  }, [driverUnderEdition, setValue]);

  const submitDriver: SubmitHandler<IUpdateDriver> = async (
    registerForm: IUpdateDriver
  ) => {
    const { isActive, ...rest } = registerForm;
    const validForm = {
      ...rest,
      isActive: isActive === "true" ? true : false,
    };

    console.log(validForm);

    updateDriver(id!, validForm);
  };

  return (
    <RegisterPageGeneric
      icon={<TbEdit className="headerIcon" />}
      title="EDITAR MOTORISTA"
    >
      <form onSubmit={handleSubmit(submitDriver)}>
        <ContainerInputs>
          <RegInput
            type={"text"}
            placeholder={"Digite o nome do motorista"}
            id={"nome"}
            label={"Nome"}
            {...register("name")}
            error={errors.name}
            value={driverName}
            onChange={(event) => {
              setDriverName(event.target.value);
            }}
          />
          <SelectInputForm
            optionsArray={cnhCategories}
            label={"Carteira de Habilitaçao"}
            {...register("licenseType")}
            error={errors.licenseType}
          />
          <RegInput
            type={"text"}
            placeholder={"xxx.xxx.xxx-xx"}
            id={"cpf"}
            label={"CPF"}
            {...register("cpf")}
            error={errors.cpf}
            value={cpfValue}
            onChange={(event) => {
              setcpfValue(cpfMask(event.target.value));
            }}
          />
          <RegInput
            type={"number"}
            placeholder={"Numero da habilitação"}
            id={"licenceNumber"}
            label={"Número CNH"}
            {...register("licenseNumber")}
            error={errors.licenseNumber}
          />
          {/* <RegInput
            type={"password"}
            placeholder={"Digite a senha do motorista"}
            id={"password"}
            label={"Senha"}
            {...register("password")}
            error={errors.password}
            defaultValue={driverUnderEdition.}
          /> */}
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
              setPhoneValue(phoneMask(event.target.value));
            }}
          />
          <RegInput
            type={"text"}
            placeholder={"Data de nascimento"}
            id={"birthYear"}
            label={"Data de nascimento"}
            {...register("birthYear")}
            error={errors.birthYear}
            value={birthYear}
            onChange={(event) => {
              setBirthYear(dateMask(event.target.value));
            }}
          />
          <SelectInputForm
            optionsArray={userStatus}
            label={"Status"}
            {...register("isActive")}
            error={errors.isActive}
          />
        </ContainerInputs>
        <div className="form__sendButton">
          <DarkBlueButton>ATUALIZAR</DarkBlueButton>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { DriverUpdate };
