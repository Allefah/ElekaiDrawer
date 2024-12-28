import { spawnSync } from 'child_process';
import { readFile } from 'fs/promises';
import path from 'path';

export default defineEventHandler(async (event) => {
    const arg1 = await readBody(event).catch(() => {})

    const pythonProcess = await spawnSync('python', [
        path.resolve('Drawer/Drawer.py'),
        'draw_circuit_from_json',
        JSON.stringify(arg1),
      ]);
     const result = pythonProcess.stdout?.toString()?.trim();
     const error = pythonProcess.stderr?.toString()?.trim();

     const status = result === 'OK';
    if (status) {
        const buffer = await readFile('./Drawer/response/schema.svg');
        return buffer.toString()
    } else {
        console.log(error)
        return { error: error }
    }
})