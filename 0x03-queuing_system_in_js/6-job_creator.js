import { createQueue } from 'kue';

const queue = createQueue();

const info = {
  phoneNumber: '07732022016',
  message: 'Hi, I am Aturiheihi Blendon, a software developer',
}

const job = queue.create('push_notification_code', info).save((err) => {
  if (!err) console.log('Notification job created:', job.id);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', (error) => console.log('Notification job failed'));
