import React from "react";

interface Option {
  value: string;
  label: string;
}

interface Props {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  options: Option[];
}

export const Select = ({ value, onChange, options }: Props) => (
  <select value={value} onChange={onChange}>
    {options.map((o) => (
      <option key={o.value} value={o.value}>
        {o.label}
      </option>
    ))}
  </select>
);
