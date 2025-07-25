import { ApplyMask } from '@utils/Mask/ApplyMask';
import type { MaskType } from '@utils/Mask/TypeMask';
import { ContainerInput } from './styles';
import { forwardRef, useId, type InputHTMLAttributes } from 'react';

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label?: string;
  errorMessage?: string;
  mask?: MaskType;
  cadeado?: boolean;
  pessoa?: boolean;
  lupa?: boolean;
  colorLabel?: string;
  backgoround?: string;
};

export const InputComponent = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      type = 'text',
      name = '',
      label = '',
      errorMessage = '',
      mask,
      lupa,
      pessoa,
      cadeado,
      backgoround,
      colorLabel,
      ...props
    },
    ref
  ) => {
    const InputId = useId();

    return (
      <div>
        <ContainerInput
          cadeado={cadeado}
          pessoa={pessoa}
          lupa={lupa}
          error={errorMessage}
          backgroundColor={backgoround}
          colorLabel={colorLabel}
        >
          {label && <label htmlFor={InputId}>{label}</label>}

          <input
            id={InputId}
            type={type}
            name={name}
            ref={ref}
            {...props}
            onChange={(e) => {
              if (mask) {
                e.target.value = ApplyMask(e, mask);
              }
              props.onChange?.(e);
            }}
          />

          {errorMessage && <p>{errorMessage}</p>}
        </ContainerInput>
      </div>
    );
  }
);
