import { ContainerInputs } from "@components/Dashboard/Driver/CreateDriver/styles";
import { RegInput } from "@components/InputForm";
import { RegisterPageGeneric } from "@components/RegisterForm";
import { SelectInputForm } from "@components/Select";
import { zodResolver } from "@hookform/resolvers/zod";
import { useDriver } from "@hooks/useDriver";
import { useTrip } from "@hooks/useTrip";
import type { ICreateTripData } from "@interfaces/trips.interface";
import { type IVehicle } from "@interfaces/vehicles.interface";
import { tripCreateFormSchema } from "@schemas/tripCreateSchema";
import { api } from "@services/api";
import { DarkBlueButton } from "@styles/Buttons";
import { dateMask } from "@utils/reserve";
import { TripStatus } from "@utils/Selects/tripStatus";
import { useEffect, useState } from "react";
import { useForm, type FieldError, type SubmitHandler } from "react-hook-form";
import { GrMapLocation } from "react-icons/gr";

const TripRegister = () => {
  const { getDriverList, driverList } = useDriver();
  const { createTrip } = useTrip();

  const vehiclesList = async () => {
    const res = await api.get("/vehicles/");

    if (res.status === 200) {
      setVehicleListData(res.data.items);
    }
  };

  const [vehicleListData, setVehicleListData] = useState<Array<IVehicle>>([]);

  const [tripDateValue, setTripDateValue] = useState("");

  const driverListSelect = driverList.map((driver) => ({
    value: driver.id,
    label: driver.name,
  }));

  const vehivleListSelect = vehicleListData.map((vehicle) => ({
    value: vehicle.id,
    label: vehicle.licensePlate,
  }));

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(tripCreateFormSchema),
  });

  const submitDriver: SubmitHandler<ICreateTripData> = async (
    registerForm: ICreateTripData
  ) => {
    createTrip();
    console.log(registerForm);
  };

  useEffect(() => {
    if (driverList.length === 0) {
      getDriverList();
      vehiclesList();
    }
  });

  return (
    <RegisterPageGeneric icon={<GrMapLocation />} title={"CADASTRO DE VIAGEM"}>
      <form onSubmit={handleSubmit(submitDriver)}>
        <ContainerInputs>
          <SelectInputForm
            optionsArray={driverListSelect}
            label={"Motorista"}
            {...register("driverId")}
            error={errors.driverId}
          />
          <RegInput
            type={"text"}
            placeholder={"DD/MM/AAAA"}
            id={"tripDate"}
            label={"Data da viagem"}
            {...register("tripDate")}
            error={errors.tripDate}
            value={tripDateValue}
            onChange={(event) => {
              setTripDateValue(dateMask(event.target.value));
            }}
          />
          <SelectInputForm
            optionsArray={vehivleListSelect}
            id={"vehicle"}
            label={"Veículo"}
            {...register("vehicleId")}
            error={errors.vehicleId}
          />
          <RegInput
            type={"time"}
            step={60}
            placeholder={"Digite a senha do motorista"}
            id={"tripHour"}
            label={"Senha"}
            {...register("tripDate")}
            error={errors.startDateTime}
          />
          <RegInput
            type={"text"}
            placeholder={"São Paulo"}
            id={"destination"}
            label={"Destino"}
            {...register("destination")}
            error={errors.destination as FieldError}
          />
          <SelectInputForm
            optionsArray={TripStatus}
            id={"tripStatus"}
            label={"Status"}
            {...register("status")}
            error={errors.status}
          />
        </ContainerInputs>
        <div className="form__sendButton">
          <DarkBlueButton>ENVIAR</DarkBlueButton>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { TripRegister };
