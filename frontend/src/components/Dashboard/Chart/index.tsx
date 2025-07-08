import { Chart, type ChartOptions } from 'chart.js/auto';
import { Doughnut } from 'react-chartjs-2';
import { ChartContainer } from './styles';
import type { IDefaultChildrenProp } from '@interfaces/default.interface';
Chart.defaults.font.family = 'Inter';

interface iDoughnutChart {
  chartData: {
    labels: string[];
    datasets: {
      label: string;
      data: number[];
      backgroundColor: string[];
      borderWidth: number;
      borderRadius: number;
      borderSkipped: boolean;
      cutout: string;
      radius: string;
    }[];
  };
}

const options: ChartOptions<'doughnut'> = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: true,
      position: 'bottom',
      labels: {
        font: {
          size: 16
        },
        usePointStyle: true,
        pointStyle: 'circle'
      }
    }
  }
};

const ChartComponent = ({ children }: IDefaultChildrenProp) => {
  return <ChartContainer>{children}</ChartContainer>;
};

const DoughnutChart = ({ chartData }: iDoughnutChart) => {
  return <Doughnut data={chartData} options={options} />;
};

export { ChartComponent, DoughnutChart };
