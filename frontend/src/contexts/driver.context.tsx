/* eslint-disable @typescript-eslint/no-unused-vars */
import type {
  ICreateDriverData,
  IDriver,
  IDriverContextProps,
  IGetDriveParams,
  IUpdateDriverData
} from '@interfaces/driver.interface';
import { createContext, type SetStateAction } from 'react';

const DriverContext = createContext<IDriverContextProps>({
  handleCreateDriver: function (
    _newDriverData: ICreateDriverData
  ): Promise<void> {
    throw new Error('Function not implemented.');
  },
  driverList: [],
  driverQuantity: 0,
  driverActive: 0,
  driverInactive: 0,
  getDriverByID: function (_id: string): Promise<void> {
    throw new Error('Function not implemented.');
  },
  driverUnderEdition: null,
  setDriverUnderEdition: function (
    _value: SetStateAction<IDriver | null>
  ): void {
    throw new Error('Function not implemented.');
  },

  deleteDriver: function (_id: string): Promise<void> {
    throw new Error('Function not implemented.');
  },
  updateDriver: function (
    _id: string,
    _driverData: IUpdateDriverData
  ): Promise<void> {
    throw new Error('Function not implemented.');
  },
  getDriverList: function ({}: IGetDriveParams): Promise<void> {
    throw new Error('Function not implemented.');
  },
  totalPages: 0,
  setTotalPages: function (_value: SetStateAction<number>): void {
    throw new Error('Function not implemented.');
  },
  apiPage: 0,
  setApiPage: function (_value: SetStateAction<number>): void {
    throw new Error('Function not implemented.');
  },
  driverName: '',
  setDriverName: function (_value: SetStateAction<string>): void {
    throw new Error('Function not implemented.');
  }
});

export { DriverContext };
