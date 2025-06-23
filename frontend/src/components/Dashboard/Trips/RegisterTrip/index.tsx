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
  interface ISelectOptions {
    value: string;
    label: string;
  }

  const { getDriverList, driverList } = useDriver();
  const { createTrip } = useTrip();
  const [vehicleListData, setVehicleListData] = useState<Array<ISelectOptions>>(
    []
  );
  const [tripDateValue, setTripDateValue] = useState("");
  const [isLoading, setIsloading] = useState(true);

  const vehiclesList = async () => {
    try {
      const res = await api.get("/vehicles/");

      if (res.status === 200) {
        const vehicleListSelect: Array<ISelectOptions> = res.data.items.map(
          (vehicle: IVehicle) => ({
            value: vehicle.id,
            label: vehicle.licensePlate,
          })
        );
        setVehicleListData(vehicleListSelect);
      }
    } catch (error) {
      console.log(error);
    } finally {
      setIsloading(false);
    }
  };

  const driverListSelect: Array<ISelectOptions> = driverList.map((driver) => ({
    value: driver.id,
    label: driver.name,
  }));

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(tripCreateFormSchema),
  });

  const submitTrip: SubmitHandler<ICreateTripData> = async (
    registerForm: ICreateTripData
  ) => {
    createTrip();
    console.log(registerForm);
  };

  useEffect(() => {
    if (isLoading === true) {
      getDriverList();
      console.log("ok");
      vehiclesList();
    }
  }, [vehicleListData, driverList]);

  return (
    <RegisterPageGeneric icon={<GrMapLocation />} title={"CADASTRO DE VIAGEM"}>
      <form onSubmit={handleSubmit(submitTrip)}>
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
            optionsArray={vehicleListData}
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
            label={"Horário"}
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
