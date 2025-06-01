export function ClearMask(value: string):string{
    return value =  value.replace(/\D/g, '');
}