const cpfMask = (value: string) => {
  return value
    .replace(/\D/g, '')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})/, '$1-$2')
    .replace(/(-\d{2})\d+?$/, '$1');
};

const dateMask = (value: string) => {
  return value
    .replace(/\D/g, '')
    .replace(/^(\d{2})(\d)/, '$1/$2')
    .replace(/^(\d{2})\/(\d{2})(\d)/, '$1/$2/$3')
    .slice(0, 10);
};

const phoneMask = (value: string) => {
  return value
    .replace(/[\D]/g, '')
    .replace(/(\d{2})(\d)/, '($1) $2')
    .replace(/(\d{5})(\d)/, '$1-$2')
    .replace(/(-\d{4})(\d+?)/, '$1');
};

const hourMask = (value: string) => {
  return value
    .replace(/[\D]/g, '')
    .replace(/(\d{2})(\d)/, '$1:$2')
    .slice(0, 5);
};

const normalizeFormString = (value: string) => {
  return value.replace(/\D/g, '');
};

const normalizeFormDate = (date: string) => {
  return date.split(`/`).reverse().join('-');
};

export {
  cpfMask,
  dateMask,
  phoneMask,
  hourMask,
  normalizeFormString,
  normalizeFormDate
};
