import createPushNotificationsJobs from "./8-job";
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();

describe('createPushNotificationsJobs', function() {
  before(() => queue.testMode.enter());
  after(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('should throw an error if jobs is not an array', (done) => {
    expect(() => createPushNotificationsJobs('Blendon is the author', queue)).to.throw('Jobs is not an array');
    done();
  });
});
